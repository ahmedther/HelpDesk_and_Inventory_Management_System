const searchUsersAndTickets = function () {
    const searchBoxes = [
        {
            'name': 'user',
            'search_box': '.user-search-box',
            'search_btn': 'user-search--btn',
            'url': 'http://127.0.0.1:8000/api/get_users/?search_value=',
            'selectHtmlTagID': '#search_user_selection',
        },
        {
            'name': 'ticket',
            'search_box': '.ticket-search-box',
            'search_btn': 'ticket-search--btn',
            'url': 'http://127.0.0.1:8000/api/get_tickets/?search_value=',
            'selectHtmlTagID': '#search_ticket_selection',
        },
    ]
    searchBoxes.forEach((el) => {
        const boxEl = document.querySelector(el.search_box)
        boxEl.addEventListener('click', (e) => searchUsersClick(e, boxEl, el))
    })

}


const searchUsersClick = function (e, boxEl, el) {
    e.preventDefault()
    const searchVal = boxEl.querySelector('.search-box-input').value
    if (!e.target.classList.contains(el.search_btn) || !searchVal) return
    // if (!boxEl.querySelector('.search-box-input').value) return
    status_update(searchVal, el)

}

const readCookie = function (name) {
    let nameEQ = name + "=";
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

const status_update = async function (search_value, el) {
    await fetch(`${el.url}${search_value}`).then(function (response) {
        return response.json()
    }).then((data) => updateSelectTag(data, el))

}

const updateSelectTag = function (data, el) {
    console.log(data)
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
    selectTagEl.addEventListener('change', () => {
        if (el.name == 'user') {
            if (selectTagEl.value == 0) userForm.forEach((el) => userFormReset(el))
            if (selectTagEl.value > 0) {
                const dataUser = data.find(user => user.id == selectTagEl.value)
                const userFormElId = [

                    { 'id': '#name', 'value': `${dataUser.first_name} ${dataUser.last_name}` },
                    { 'id': '#requester_pr_number', 'value': dataUser.pr_number },
                    { 'id': '#requester_designation', 'value': dataUser.designation },
                    { 'id': '#requester_department', 'value': dataUser.department },
                    { 'id': '#requester_email', 'value': dataUser.email },
                    { 'id': '#requester_extension', 'value': dataUser.extension_number },
                    { 'id': '#requester_phone_number', 'value': dataUser.mobile_number },

                ]
                userFormElId.forEach((el_id) => userFormUpdation(el_id.id, el_id.value, userForm))
            }
        }
    })
}


const userFormUpdation = function (selectorName, inputValue, userForm) {
    const element = document.querySelector(selectorName)
    element.setAttribute('disabled', true)
    element.value = inputValue
    userForm.push(element)

}

const userFormReset = function (element) {
    element.removeAttribute('disabled')
    element.value = ""
}


searchUsersAndTickets()
