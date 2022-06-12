const isEmpty = str => !str.trim().length;

document.addEventListener('input', event => {
    const nameValue = document.getElementById("name").value;
    const emailValue = document.getElementById("email").value;
    const phoneValue = document.getElementById("phone").value;
    const addressValue = document.getElementById("address").value;
    const cityValue = document.getElementById("city").value;
    const countryValue = document.getElementById("country").value;

    const updateButton = document.getElementById('updateButton')
    if (isEmpty(nameValue) &&
        isEmpty(emailValue) &&
        isEmpty(phoneValue) &&
        isEmpty(addressValue) &&
        isEmpty(cityValue) &&
        isEmpty(countryValue)) {
        updateButton.disabled = true
    } else {
        updateButton.disabled = false
    }
})