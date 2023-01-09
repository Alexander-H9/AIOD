const username_input = document.querySelector("#username-input");
const password_input = document.querySelector("#password-input");
const login_btn = document.querySelector("#login-btn")

login_btn.addEventListener("click", async () => await login());

async function login() {
    var username = username_input.value;
    var password = password_input.value;
    let response = await fetch("/login?username="+username+"&password="+password, {
        method: "POST"
    });
    if (response.status == 200) {
        let res = await response.text()
        console.log(res)
    } else {
        console.log("Failed")
    }
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
  
    var input = $('.validate-input .input100');
    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });

    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }
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