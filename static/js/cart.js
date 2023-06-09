


console.log('cart.js is working')



var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function() {
        var pizzaId = this.dataset.pizza || null
        var action = this.dataset.action
        console.log('pizzaId:', pizzaId, 'Action:', action)
            console.log('USER', user)
        if (user === 'AnonymousUser'){
            console.log('User is not authenticated')
        }else {
            updateUserOrder(pizzaId, action)
        }
    })
}

function updateUserOrder(pizzaId, action) {
    console.log('User is logged in, sending data...')
    var url = '/cart/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body:JSON.stringify({'pizzaId': pizzaId, 'action': action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}


var updateBtns2 = document.getElementsByClassName('update-offer')

console.log(updateBtns2)

for (i = 0; i < updateBtns2.length; i++){
    updateBtns2[i].addEventListener('click', function() {
        var offerId = this.dataset.offer || null
        var action2 = this.dataset.action2
        console.log('offerId:', offerId, 'Action2:', action2)
            console.log('USER', user)
        if (user === 'AnonymousUser'){
            console.log('User is not authenticated')
        }else {
            updateUserOrderOffer(offerId, action2)
        }
    })
}

function updateUserOrderOffer(offerId, action2) {
    console.log('User is logged in, sending data...')
    var url = '/cart/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body:JSON.stringify({'offerId': offerId, 'action2': action2})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}




/* Write a function that listens for a click on the form-button in checkout.html, collects the necessary information and redirects to the payment page */

function checkoutForm(){
    const form = document.getElementById('form');
    form.addEventListener('submit', function(e){
        e.preventDefault()
        console.log('Form submitted...')
        document.getElementById('form-button').classList.add('hidden')
        document.getElementById('payment-info').classList.remove('hidden')
        let email = document.getElementsByName('email').item(0).value
        let address = document.getElementsByName('address').item(0).value
        let city = document.getElementsByName('city').item(0).value
        let zipcode = document.getElementsByName('zipcode').item(0).value
        console.log(name, email, address, city, zipcode)
        let url = '/cart/payment/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken
            },
            body:JSON.stringify({'form': form, 'name': name, 'email': email, 'address': address, 'city': city, 'zipcode': zipcode})
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)

        })
    })
}

function sumbitFormData(){
    console.log('Data is being submitted')
    var userFormData = {
        'name': null,
        'email': null,
        'address': null,
        'city': null,
        'zipcode': null,
    }
    let form = document.getElementById('form');
    var shippingInfo = {
        'name': form.name.value,
        'email': form.email.value,
        'address': form.address.value,
        'city': form.city.value,
        'zipcode': form.zipcode.value,
    }
    for (var i = 0; i < form.length - 1; i++){
        userFormData[form[i].name] = form[i].value
    }
    console.log('userFormData', userFormData)
    return userFormData
}
/*
function getContactInfo():{name: string, email: string, address: string, city: string, state: string, zipcode: string}{
    console.log("You're here")



    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const address = document.getElementById('address').value;
    const city = document.getElementById('city').value;
    const zipcode = document.getElementById('zipcode').value;
    let url = '/cart/payment/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken
            },
            body:JSON.stringify({ 'name': name, 'email': email, 'address': address, 'city': city, 'zipcode': zipcode})
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
    console.log("Hello test")
    console.log(name, email, address, city, zipcode)
    return name, email, address, city, zipcode
})
}*/
