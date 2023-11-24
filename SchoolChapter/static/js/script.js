function getCookie(name) {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return cookieValue ? cookieValue.pop() : '';
}

const submit_mcq = () => {
  const checkedValues = document.querySelectorAll(".cb");
  const options = [];
  checkedValues.forEach((checkbox) => {
    options.push({ option_id: checkbox.id, checked: checkbox.checked });
  });

  const csrftoken = getCookie('csrftoken');
  const xhr = new XMLHttpRequest();

  // set the HTTP method and URL for the request
  xhr.open("POST", "/topic/mcq-submittion/");

  // set the Content-Type header to indicate that we're sending JSON data
  xhr.setRequestHeader("Content-Type", "application/json");

  // set the CSRF token header
  xhr.setRequestHeader("X-CSRFToken", csrftoken);

  // convert the data object to a JSON string
  const jsonData = JSON.stringify(options);

  // set a callback function to handle the response from the server
  xhr.onload = () => {
    if (xhr.status === 200) {
      // handle successful response here
      location.reload()
    } else {
      // handle error response here
      console.error(xhr.statusText);
      location.reload()
    }
  };

  // send the request with the JSON data in the request body
  xhr.send(jsonData);
};


function extractIdAndNumber(str) {
  const regex = /(\d+)__op(\d+)/;
  const match = str.match(regex);
  if (match) {
    const id = parseInt(match[1]);
    const number = parseInt(match[2]);
    return { id, number };
  } else {
    return null;
  }
}

const submit_fomcqs = () => {
  console.log("submitting fomcqs")
  var listOfMcqResponses = []
  var elements = document.getElementsByClassName("chk-option");
  for (var element of elements) {
    if (element.checked) {
      const result = extractIdAndNumber(element.id);
      listOfMcqResponses.push(result);
    }
  }

  if (listOfMcqResponses.length > 0) {

    const csrftoken = getCookie('csrftoken');
    const xhr = new XMLHttpRequest();

    // set the HTTP method and URL for the request
    xhr.open("POST", "/topic/fomcq-submittion/");

    // set the Content-Type header to indicate that we're sending JSON data
    xhr.setRequestHeader("Content-Type", "application/json");

    // set the CSRF token header
    xhr.setRequestHeader("X-CSRFToken", csrftoken);

    // convert the data object to a JSON string
    const jsonData = JSON.stringify(listOfMcqResponses);

    // set a callback function to handle the response from the server
    xhr.onload = () => {
      if (xhr.status === 200) {
        // handle successful response here
        location.reload()
      } else {
        // handle error response here
        console.error(xhr.statusText);
        location.reload()
      }
    };

    // send the request with the JSON data in the request body
    xhr.send(jsonData);
  }


}