const togglePasswordShow = () => {
    const passwordInput = document.getElementById("password");
    if (passwordInput.type === "password" && passwordInput.value !== "") {
        document.getElementById("password").type = "text"
        document.getElementById("passwordEye").className = "far fa-eye-slash fa-lg"
    } else {
        document.getElementById("password").type = "password"
        document.getElementById("passwordEye").className = "far fa-eye fa-lg"
    }
}