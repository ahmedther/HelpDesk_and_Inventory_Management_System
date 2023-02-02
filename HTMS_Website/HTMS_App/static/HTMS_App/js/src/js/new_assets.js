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
        element.classList.remove('disabled')
        element.value = ""
        return
    }

    
    element.removeAttribute('disabled')
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


const disableNonEssElements = function () {
    const selectCurrentStatus = document.querySelector('#asset_current_status')
    selectCurrentStatus.addEventListener('change', () => {
        if (selectCurrentStatus.value != 'in-use') {
            const elementIds = [...get_elementsID(undefined, "user"), ...get_elementsID(undefined, "ticket")]
            elementIds.push({ 'id': '#search_user' }, { 'id': '#search_ticket' })
            elementIds.forEach((elIds) => userFormUpdation(elIds.id, ""))
            submitButtonPosition('.create_assest-form')
        }
        if (selectCurrentStatus.value == 'in-use') {
            const elementIds = [...get_elementsID(undefined, "user"), ...get_elementsID(undefined, "ticket")]
            elementIds.push({ 'id': '#search_user' }, { 'id': '#search_ticket' })
            elementIds.forEach((elIds) => {
                const elementId = document.querySelector(elIds.id)
                userFormReset(elementId)
            })
            submitButtonPosition('.asset_user_form')
        }
    })
}

const submitButtonPosition = function (targetClass) {
    const subBtn = document.querySelector('.submit-button')
    const targetEl = document.querySelector(targetClass)
    subBtn.remove()
    targetEl.appendChild(subBtn)
}

disableNonEssElements()
searchUsersAndTickets()
