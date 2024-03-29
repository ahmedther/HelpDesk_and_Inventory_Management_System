export const scroller = function () {
  const progress = document.querySelector(".progressbar");
  const totalHeight = document.body.scrollHeight - window.innerHeight;
  window.onscroll = function () {
    const progressHeight = (window.pageYOffset / totalHeight) * 100;
    progress.style.height = progressHeight + "%";
  };
};


const randomColorNumber = function () {
  const color = Math.floor(Math.random() * 256)
  return color
}

export const profileRandomColor = function () {
  const profileElement = document.querySelectorAll(".requester-profile-photo");
  profileElement.forEach((el) => colorChanger(el));

  const paginateEl = document.querySelectorAll(".page-active");
  paginateEl.forEach((el) => colorChanger(el));
};

function colorChanger(el) {
  // const a = el.parentNode.parentNode.children[4].firstElementChild
  // const b = getComputedStyle(a)
  // const c = b['background']
  // const red = randomColorNumber()
  // const red1 = randomColorNumber()
  // const blue = randomColorNumber()
  // const blue1 = randomColorNumber()
  // const green = randomColorNumber()
  // const green1 = randomColorNumber()
  //  el.style.background = `linear-gradient(138deg, rgba(${red}, ${blue}, ${green}, 1) 0%, rgba(${red1}, ${blue1}, ${green1}, 1) 100% )`
  const colorList = [
    "#fca311", //yellow
    "#FFDD00", // yellow light
    "#FF4301", //orange dark
    "#F66B0E", //orange light
    "#ff006e", // dark pink
    "#F806CC", // light pink
    "#31E1F7", // sky blue
    "#0096FF", // blue
    "#00B7A8", // aqua blue teal
    "#3DB2FF",//light blue
    "#113CFC", // cco blue
    "#3B44F6", // indigo
    "#000000", //dark black
    "#4C0070", // dark purple
    "#8200FF", // light purple
    "#45046A",//violet
    "#FF0000", //red
    "#379237",//dark green
    "#49FF00", // light green
    "#A6CB12", //off green
    '#864000', //brown
    "#290001", // dark brown
    "#6A492B", //chikku brown
    "#696464",//grey dark
    "#414141",//grey light
    "#FF7F5B", // peach

  ];
  const color = Math.floor(Math.random() * colorList.length);
  //const color1 = Math.floor(Math.random() * colorList.length);
  // el.style.background = colorList[color]
  const backGradient = `linear-gradient(138deg, ${colorList[color]}90 0%, ${colorList[color]} 100%)`;
  el.style.background = backGradient;
  // el.style.background = colorList[color];
  //el.style.background = c
}


function readCookie(name) {
  let nameEQ = name + "=";
  let ca = document.cookie.split(';');
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}



export const status_update = async function () {
  await fetch('http://172.20.100.81:8004/api/get_status/?format=json').then(function (response) {
    return response.json()
  }).then((data) => status_working(data))

}

const status_working = function (data1) {
  let data = data1
  data = data1.filter(function (item) {
    if (item.status_name == 'Open' || item.status_name == 'Assigned') return null
    else return item.status_name
  })
  const csrftoken = readCookie('csrftoken');
  const slugify = require('slugify')
  const html = data.map((status) => status_html(status, slugify))
  const statusEL = document.querySelectorAll('.display-ticket-status');
  statusEL.forEach((el) => status_instert(el, html, csrftoken, slugify))
}

const status_html = function (status, slugify) {
  let html = `<a data-status-value="${status.status_name}"class="change-status--link" href="#">
                      <div class="display-status-${slugify(status.status_name).toLowerCase()}">
                          <div class='display-status-text'>${status.status_name}</div>
                      </div>
                  </a>`
  return html
}

const status_instert = function (el, html, csrftoken, slugify) {
  if (el.previousElementSibling.firstElementChild.innerHTML == 'None'
    || el.querySelector('.display-status-text').innerHTML == 'Closed'
    || el.querySelector('.display-status-text').innerHTML == 'Unresolved'
    || el.classList.contains("non_it")) {

    return
  }

  el.addEventListener('click', (e) => statusEvent(e, el, html, csrftoken, slugify))
}


function statusEvent(e, el, html, csrftoken, slugify) {
  e.preventDefault();
  deleteTextArea()
  delete_dropDown()
  if (el.querySelector('.display-status-text').innerHTML == 'Closed' || el.querySelector('.display-status-text').innerHTML == 'Unresolved') {
    return
  }
  el.insertAdjacentHTML('beforebegin', `<div class="change-status--container">` + html.join("") + `</div>`
  )
  dropdownBtnClick(el, csrftoken, slugify)
}

function dropdownBtnClick(status_element, csrftoken, slugify) {
  const dropdownBtn = document.querySelectorAll(".change-status--link")
  dropdownBtn.forEach((el) => status_post_request(el, status_element, csrftoken, slugify))

}

const status_post_request = function (el, status_element, csrftoken, slugify) {
  el.addEventListener('click', (e) => {
    post_format(e, el, status_element, csrftoken, slugify)
  })
}

const post_format = async function (e, el, status_element, csrftoken, slugify) {
  e.preventDefault();
  const el_id = el.closest('.ticket-main-row')
  if (el.dataset.statusValue == 'On Hold' || el.dataset.statusValue == 'Unresolved') {
    onHoldReason(el_id, el, status_element, csrftoken, slugify)
  }

  if (el.dataset.statusValue != 'On Hold' && el.dataset.statusValue != 'Unresolved') post_to_databae(el_id, el, status_element, csrftoken, slugify)
}

async function post_to_databae(el_id, el, status_element, csrftoken, slugify) {

  await fetch("http://172.20.100.81:8004/api/post_status/", {

    // Adding method type
    method: "POST",

    // Adding body or contents to send
    body: JSON.stringify({
      id: el_id.dataset.id,
      status: el.dataset.statusValue
    }),

    // Adding headers to the request
    headers: {
      "Content-type": "application/json; charset=UTF-8",
      "X-CSRFToken": csrftoken
    }
  })

    // Converting to JSON
    // .then(response => response.json())

    // Displaying results to console
    .then(function (response) {
      // console.log(json)
      status_element.firstElementChild.classList = `display-status-${slugify(el.dataset.statusValue).toLowerCase()}`
      delete_dropDown()
      status_element.querySelector('.display-status-text').innerHTML = el.dataset.statusValue

    });

}

function delete_dropDown() {
  const drop_container = document.querySelectorAll('.change-status--container')
  drop_container.forEach((el) => addAnimeDelete(el))

}

function deleteTextArea() {
  const reasonTextArea = document.querySelectorAll('.on-hold--post')
  reasonTextArea.forEach((el) => addAnimeDelete(el))

}

const addAnimeDelete = function (el) {
  el.style.animation = '500ms dropdownStatusFade'
  setTimeout(removefunc, '500', el)
}

const removefunc = function (el) {
  el.remove()
}

const onHoldReason = function (el_id, el, status_element, csrftoken, slugify) {
  const onHoldHtml = `<div class="on-hold--post">
  <label  class='on-hold--label' for='description'>Reason for The ${el.dataset.statusValue} Status</label>
  <textarea autofocus class='on-hold--post-textarea' rows="5" cols="33" type="text" name="description" id="description"
    placeholder="Why is this issue put ${el.dataset.statusValue}?"></textarea>
  <button type='submit' class='on-hold--submit-button'>
      <span class='btn--add btn--text'>Submit</span>
  </button>
</div>`

  const holdCont = el.closest('.ticket-main-row')
  const tick_stat = holdCont.querySelector('.display-ticket-status')
  tick_stat.insertAdjacentHTML('beforebegin', onHoldHtml)
  const textarea = document.querySelector('.on-hold--post')
  textarea.addEventListener('click', function (e) {
    e.preventDefault()
    const textvalueEl = this.querySelector('.on-hold--post-textarea')
    const submitButton = document.querySelector('.on-hold--submit-button')
    submitButton.removeEventListener('click', postReasonToDb)
    submitButton.addEventListener('click', postReasonToDb(e, textvalueEl, holdCont, el_id, el, status_element, csrftoken, slugify))
  })

}

const postReasonToDb = function (e, textvalueEl, holdCont, el_id, el, status_element, csrftoken, slugify) {
  e.preventDefault()
  if (textvalueEl.value)
    fetch("http://172.20.100.81:8004/api/post_reason_on_hold/", {

      // Adding method type
      method: "POST",

      // Adding body or contents to send
      body: JSON.stringify({
        id: holdCont.dataset.id,
        reson_for_hold: textvalueEl.value
      }),

      // Adding headers to the request
      headers: {
        "Content-type": "application/json; charset=UTF-8",
        "X-CSRFToken": csrftoken
      }
    })

      // Converting to JSON
      // .then(response => response.json()).then((json) => console.log(json))
      .then(response => deleteTextArea()).then((res) => post_to_databae(el_id, el, status_element, csrftoken, slugify))
}
export function closeDropdown() {
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.display-ticket-status')
      && !e.target.closest('.change-status--container')
      && !e.target.closest('.on-hold--post')) {
      deleteTextArea()
      delete_dropDown()
    }
  })
}


///////////////////////////
// Search Users and Tickets
///////////////////////////

export const searchUsersAndTickets = function () {
  const searchBoxes = [
    {
      'name': 'user',
      'search_box': '.user-search-box',
      'search_btn': 'user-search--btn',
      'url': 'http://172.20.100.81:8004/api/get_users/?search_value=',
      'selectHtmlTagID': '#search_user_selection',
    },
    {
      'name': 'ticket',
      'search_box': '.ticket-search-box',
      'search_btn': 'ticket-search--btn',
      'url': 'http://172.20.100.81:8004/api/get_tickets/?search_value=',
      'selectHtmlTagID': '#search_ticket_selection',
    },
  ]
  searchBoxes.forEach((el) => {
    const boxEl = document.querySelector(el.search_box)
    try {

      boxEl.addEventListener('click', (e) => searchUsersClick(e, boxEl, el))
    } catch (error) {
      // code to handle the error
      console.error(error);
    }

  })

}


const searchUsersClick = function (e, boxEl, el) {
  e.preventDefault()
  const searchVal = boxEl.querySelector('.search-box-input').value
  if (!e.target.classList.contains(el.search_btn) || !searchVal) return
  // if (!boxEl.querySelector('.search-box-input').value) return
  status_update_asset(searchVal, el)

}


const status_update_asset = async function (search_value, el) {
  await fetch(`${el.url}${search_value}`).then(function (response) {
    return response.json()
  }).then((data) => updateSelectTag(data, el))

}

const updateSelectTag = function (data, el) {
  data = Object.values(data)
  const selectTagEl = document.querySelector(el.selectHtmlTagID)
  const selectTagElParent = selectTagEl.previousElementSibling
  selectTagEl.remove()
  let html = ''
  if (el.name == 'user') {
    html += `<select  name="search_user_selection" class="select" id="${el.selectHtmlTagID.toString().slice(1)}">
              <option disabled selected hidden value=""> --${data.length > 0 ? 'Select User (' + data.length : ' No Data ( No'} Users Found) -- </option> 
              <option value="0"> &#128472 Reset User's Fields</option>`
    data.forEach(user => {
      html += `<option value="${user.id}">${user.first_name} ${user.last_name} (${user.username})</option>`
    });

  }
  if (el.name == 'ticket') {
    html += `<select  name="search_ticket_selection" class="select" id="${el.selectHtmlTagID.toString().slice(1)}">
          <option disabled selected hidden value=""> --${data.length > 0 ? 'Select Ticket (' + data.length : ' No Data ( No'} Tickets Found) -- </option> 
          <option value="0"> &#128472 Reset Ticket's Fields</option>`
    data.forEach(ticket => {
      html += `<option value="${ticket.id}">No. ${ticket.id} | ${ticket.requester_name} | ${ticket.request_category}</option>`
    });

  }
  html += `</select>`
  selectTagElParent.insertAdjacentHTML('afterend', html)
  UserFormUpdate(data, el)
}

const UserFormUpdate = function (data, el) {
  const selectTagEl = document.querySelector(el.selectHtmlTagID)
  const userForm = []
  const ticketForm = []
  selectTagEl.addEventListener('change', () => {
    if (el.name == 'user') {
      if (selectTagEl.value == 0) userForm.forEach((el) => userFormReset(el))
      if (selectTagEl.value > 0) {
        const dataUser = data.find(user => user.id == selectTagEl.value)
        const userFormElId = get_elementsID(dataUser, el.name)
        userFormElId.forEach((el_id) => userFormUpdation(el_id.id, el_id.value, userForm))
      }
    }

    if (el.name == 'ticket') {
      if (selectTagEl.value == 0) ticketForm.forEach((el) => userFormReset(el))
      if (selectTagEl.value > 0) {
        const dataTicket = data.find((ticket) => ticket.id == selectTagEl.value)
        const ticketFormElId = get_elementsID(dataTicket, el.name)
        ticketFormElId.forEach((el_id) => userFormUpdation(el_id.id, el_id.value, ticketForm))

      }
    }
  })
}


const userFormUpdation = function (selectorName, inputValue, userForm = null) {
  if (selectorName == "#request_status") {
    const element = document.querySelector(selectorName)
    element.classList.add('disabled')
    element.value = inputValue
    if (userForm) userForm.push(element)
    return
  }

  const element = document.querySelector(selectorName)
  element.setAttribute('disabled', true)
  element.value = inputValue
  element.classList.add('disabled')
  if (userForm) userForm.push(element)



}

const userFormReset = function (element) {
  if (element.id == 'request_status') {
    // element.classList.remove('disabled')
    element.value = ""
    return
  }


  element.removeAttribute('disabled')
  element.readOnly = false;
  element.value = ""
  element.classList.remove('disabled')


}



const get_elementsID = function (data, request_type) {
  if (!data) {
    data = {}
  }
  if (request_type == 'ticket') {
    return [
      { 'id': '#request_type', 'value': data.request_type },
      { 'id': '#request_status', 'value': data.request_status },
      { 'id': '#request_mode', 'value': data.request_mode },
      { 'id': '#request_priority', 'value': data.request_priority },
      { 'id': '#request_category', 'value': data.request_category },
      { 'id': '#request_technician', 'value': data.request_technician_id },
      { 'id': '#subject', 'value': data.subject },
      { 'id': '#location', 'value': data.location }
    ]
  }

  if (request_type == 'user') {
    return [

      { 'id': '#name', 'value': `${data.first_name} ${data.last_name}` },
      { 'id': '#requester_pr_number', 'value': data.pr_number },
      { 'id': '#requester_designation', 'value': data.designation },
      { 'id': '#requester_department', 'value': data.department },
      { 'id': '#requester_email', 'value': data.email },
      { 'id': '#requester_extension', 'value': data.extension_number },
      { 'id': '#requester_phone_number', 'value': data.mobile_number },

    ]
  }


}


export const disableNonEssElements = function () {
  try {
    const selectCurrentStatus = document.querySelector('#asset_current_status')
    selectCurrentStatus.addEventListener('change', () => {
      if (selectCurrentStatus.value != 'In Use') {
        const elementIds = [...get_elementsID(undefined, "user"), ...get_elementsID(undefined, "ticket")]
        elementIds.push({ 'id': '#search_user' }, { 'id': '#search_ticket' })
        elementIds.forEach((elIds) => userFormUpdation(elIds.id, ""))
        submitButtonPosition('.create_assest-form')
      }
      if (selectCurrentStatus.value == 'In Use') {
        const elementIds = [...get_elementsID(undefined, "user"), ...get_elementsID(undefined, "ticket")]
        elementIds.push({ 'id': '#search_user' }, { 'id': '#search_ticket' })
        elementIds.forEach((elIds) => {
          const elementId = document.querySelector(elIds.id)
          userFormReset(elementId)
        })
        submitButtonPosition('.asset_user_form')
      }
    })
  } catch (error) {
    // code to handle the error
    console.error(error);
  }

}

const submitButtonPosition = function (targetClass) {
  const subBtn = document.querySelector('.submit-button')
  const targetEl = document.querySelector(targetClass)
  subBtn.remove()
  targetEl.appendChild(subBtn)
}























// export function paginationBtnClick() {
//   const search_box = document.getElementById('search-box-id')
//   const pagi_btn = document.querySelectorAll('.pagi-link')
//   if (search_box) {
//     pagi_btn.forEach(function (el) {

//       el.addEventListener('click', (e) => {
//         e.preventDefault()
//         const targetEl = el.closest('.pagi-link')
//         search_box.innerHTML += `<input value='${targetEl.dataset.page}' name='page' hidden>`x
//         search_box.submit()

//       })
//     })
//   }
// }

// import * as pg from 'pg';  // import pg

// const { Client } = require('pg')

// const client = new Client({
//     user: "postgres",
//     host: "172.20.100.81",
//     database: "HTMS_database",
//     password: "ahmed",
//     port: "5432",
// })

// client.connect();

// client.query(`SELECT * FROM public."HTMS_App_requests"
// ORDER BY id ASC `, (err, result) => {
//     if (err) {
//         console.log(err.message);
//     }
//     else {
//         console.log(result.rows);
//     }
// })
// let test
// const status_update = async function () {
//   await fetch('http://172.20.100.81:8004/api/get_status/?format=json').then(function (response) {
//     return response.json()
//   }).then(function (data) {

//     const ne1w = data.map(function (status) {
//       const slugify = require('slugify')
//       let html = `<li><div class="display-status-${slugify(status.status_name).toLowerCase()}">
//                         <div class='display-status-text'>${status.status_name}</div>
//                       </div>
//                   </li>`
//       return html
//     }
//     )
//     test = ne1w
//   })



// }

// const statusEL = document.querySelectorAll('.display-ticket-status');
// statusEL.forEach(function (el) {
//   el.addEventListener('click', function (e) {
//     e.preventDefault();
//     console.log(test[0])
//     el.insertAdjacentHTML('afterbegin', `<ul class="change-status--container">` + test.join("") + ` </ul >`
//     )
//   }

//   )
// }

// )