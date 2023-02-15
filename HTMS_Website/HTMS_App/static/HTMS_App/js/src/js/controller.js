import * as helper from "./helper.js";


helper.scroller();

helper.profileRandomColor()

helper.status_update()

helper.closeDropdown()

helper.disableNonEssElements() // on Add Asset Page

helper.searchUsersAndTickets()


// helper.paginationBtnClick()

// function readCookie(name) {
//     let nameEQ = name + "=";
//     let ca = document.cookie.split(';');
//     for (let i = 0; i < ca.length; i++) {
//         let c = ca[i];
//         while (c.charAt(0) == ' ') c = c.substring(1, c.length);
//         if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
//     }
//     return null;
// }

// const csrftoken = readCookie('csrftoken');
// const slugify = require('slugify')

// let test
// const status_update = async function () {
//     await fetch('http://127.0.0.1:8000/api/get_status/?format=json').then(function (response) {
//         return response.json()
//     }).then(function (data) {

//         const ne1w = data.map(function (status) {

//             let html = `<a data-status-value="${status.status_name}"class="change-status--link" href="#">
//                             <div class="display-status-${slugify(status.status_name).toLowerCase()}">
//                                 <div class='display-status-text'>${status.status_name}</div>
//                             </div>
//                         </a>`
//             return html
//         }
//         )
//         test = ne1w
//     })



// }

// const statusEL = document.querySelectorAll('.display-ticket-status');
// statusEL.forEach(function (el) {
//     el.addEventListener('click', function (e) {
//         e.preventDefault();
//         el.insertAdjacentHTML('beforebegin', `<div class="change-status--container">` + test.join("") + `</div>`
//         )
//         const status_value = dropdownBtnClick(el)

//     }

//     )

// }


// )

// function dropdownBtnClick(status_element) {
//     const dropdownBtn = document.querySelectorAll(".change-status--link")
//     dropdownBtn.forEach(function (el) {
//         el.addEventListener('click', function (e) {
//             e.preventDefault();
//             const el_id = el.closest('.ticket-main-row')

//             fetch("http://127.0.0.1:8000/api/post_status/", {

//                 // Adding method type
//                 method: "POST",

//                 // Adding body or contents to send
//                 body: JSON.stringify({
//                     id: el_id.dataset.id,
//                     status: el.dataset.statusValue
//                 }),

//                 // Adding headers to the request
//                 headers: {
//                     "Content-type": "application/json; charset=UTF-8",
//                     "X-CSRFToken": csrftoken
//                 }
//             })

//                 // Converting to JSON
//                 .then(response => response.json())

//                 // Displaying results to console
//                 .then(function (json) {
//                     console.log(json)
//                     console.log(status_element)
//                     status_element.firstElementChild.classList = `display-status-${slugify(el.dataset.statusValue).toLowerCase()}`
//                     el.closest('.change-status--container').remove()
//                     status_element.querySelector('.display-status-text').innerHTML = el.dataset.statusValue
//                 });


//         })
//     })

// }


// status_update()