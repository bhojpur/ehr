document.addEventListener("input", event => {
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");
    const iconMatch = document.getElementById("match")

    // if both password inputs empty or only confirm is empty -> keep background white
    if ((password.value.length === 0 && confirmPassword.value.length === 0) || confirmPassword.value.length === 0) {
        password.style.backgroundColor = "#FFFFFF"
        confirmPassword.style.backgroundColor = "#FFFFFF"
        iconMatch.className = ""
    } else if (password.value === confirmPassword.value && password.value.length > 4) {
        password.style.backgroundColor = "#e1ffe0"
        confirmPassword.style.backgroundColor = "#e1ffe0"
        iconMatch.className = "fas fa-check"
    } else {
        password.style.backgroundColor = "#ffdfd5"
        confirmPassword.style.backgroundColor = "#ffdfd5"
        iconMatch.className = "fas fa-times"
    }
})

const checkPasswordMatching = () => {
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");
    const iconMatch = document.getElementById("match")
    const isMatching = password.value === confirmPassword.value

    if (!isMatching) {
        confirmPassword.style.backgroundColor = "#CD5C5C"
        iconMatch.className = "fas fa-exclamation"
    }

    return isMatching
}