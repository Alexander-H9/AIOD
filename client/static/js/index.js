const username_input = document.querySelector("#username-input");
const password_input = document.querySelector("#password-input");
const login_btn = document.querySelector("#login-btn");
const login_span = document.querySelector("#login-span");

login_btn.addEventListener("click", async () => await loginAccount());

async function loginAccount() {
    var username = username_input.value;
    var password = password_input.value;

    let formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    if (username !== "" && password !== ""){
        let response = await fetch("/account/login", {
            method: "POST",
            body:formData
        });
        if (response.status == 200) {
            let res = await response.json();
            console.log(res);
            let flag = res[0];
            let status = res[1];
            if (flag == 0) {
                login_span.style.color = "#32cd32";
                login_span.innerHTML = "<i class='fas fa-check'></i>";
                await new Promise(r => setTimeout(r, 1000));
                window.location.replace("/home");
            } else {
                login_span.style.color = "#f50537";
                login_span.innerHTML = "<i class='fas fa-xmark'></i> "+status;
            }
        } else {
            login_span.style.color = "#f50537";
            login_span.textContent = "Error";
        }
    } else if (username == "" && password == ""){
        showValidate("#username-input");
        showValidate("#password-input");
    } else if (username == ""){
        showValidate("#username-input");
    } else if (password == ""){
        showValidate("#password-input");
    } else {
        alert("fatal error");
    }
    await new Promise(r => setTimeout(r, 2000));
    login_span.textContent = "";
}

function showValidate(input) {
    var thisAlert = $(input).parent();
    $(thisAlert).addClass('alert-validate');
}

(function ($) {

    $('.input100').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })    
    })

    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    var showPass = 0;
    $('.btn-show-pass').on('click', function(){
        if(showPass == 0) {
            $(this).next('input').attr('type','text');
            $(this).find('i').removeClass('fa-solid fa-eye');
            $(this).find('i').addClass('fa-solid fa-eye-slash');
            showPass = 1;
        }
        else {
            $(this).next('input').attr('type','password');
            $(this).find('i').removeClass('fa-solid fa-eye-slash');
            $(this).find('i').addClass('fa-solid fa-eye');
            showPass = 0;
        }  
    });
})(jQuery);