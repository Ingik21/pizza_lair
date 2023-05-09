


console.log('cart.js is working')



var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function() {
        var pizzaId = this.dataset.pizza
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


var updateBtns2 = document.getElementsByClassName('update-cart-offer')

for (i = 0; i < updateBtns2.length; i++){
    updateBtns2[i].addEventListener('click', function() {
        var offerId = this.dataset.offer
        var action = this.dataset.action
        console.log('offerId:', offerId, 'Action:', action)
            console.log('USER', user)
        if (user === 'AnonymousUser'){
            console.log('User is not authenticated')
        }else {
            updateUserOrderOffer(offerId, action)
        }
    })
}

function updateUserOrderOffer(offerId, action) {
    console.log('User is logged in, sending data...')
    var url = '/cart/update_item_offer/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body:JSON.stringify({'offerId': offerId, 'action': action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
    })
}




/* Write a function that listens for a click on the form-button in checkout.html, collects the necessary information and redirects to the payment page */

function checkoutForm(){
    const form = document.getElementById('checkout-form');
    form.addEventListener('submit', function(e){
        e.preventDefault()
        console.log('Form submitted...')
        var name = document.getElementById('name').value
        var email = document.getElementById('email').value
        var address = document.getElementById('address').value
        var city = document.getElementById('city').value
        var state = document.getElementById('state').value
        var zipcode = document.getElementById('zipcode').value
        console.log(name, email, address, city, state, zipcode)
        var url = '/cart/checkout/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken
            },
            body:JSON.stringify({'form': form, 'name': name, 'email': email, 'address': address, 'city': city, 'state': state, 'zipcode': zipcode})
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
    })
}

function getContactInfo():{name: string, email: string, address: string, city: string, state: string, zipcode: string}{
    console.log("You're here")



    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const address = document.getElementById('address').value;
    const city = document.getElementById('city').value;
    const state = document.getElementById('state').value;
    const zipcode = document.getElementById('zipcode').value;

    console.log("Hello test")
    console.log(name, email, address, city, state, zipcode)
    return name, email, address, city, state, zipcode
}