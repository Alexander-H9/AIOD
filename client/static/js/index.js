const email_input = document.querySelector("#email-input");
const password_input = document.querySelector("#password-input");
const login_btn = document.querySelector("#login-btn")

login_btn.addEventListener("click", async () => await login());

async function login() {
    var email = email_input.value;
    var password = password_input.value;
    let response = await fetch("/login?email="+email+"&password="+password, {
        method: "POST"
    });
    if (response.status == 200) {
        let res = await response.json()
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

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

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