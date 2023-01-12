const upload_btn = document.querySelector("#upload-btn");
const upload_input = document.querySelector("#upload-input");
const upload_span = document.querySelector("#upload-span");
const result_span = document.querySelector("#result-span");

const select_functionality = document.querySelector("#select-functionality")

upload_btn.addEventListener("click", async () => await uploadFile());

async function uploadFile() {
    let functionality = select_functionality.value;
    let img = upload_input.files[0];
    
    if (typeof img !== 'undefined')  {
        let formData = new FormData();
        formData.append("functionality", functionality);
        formData.append("image", img);

        upload_span.innerHTML = '<img src="./static/loader2.gif" id="loading-gif" class="img-fluid" width="50"></img>';
        let response = await fetch("/media/upload", {method: "POST", body:formData});
        await new Promise(r => setTimeout(r, 5000));
        upload_span.innerHTML = "";
        if (response.status == 200) {
            let res = await response.json()
            let flag = res[0];
            let status = res[1];
            console.log(flag, status)
            if (flag == 0) {
                upload_span.style.color = "#32cd32";
                upload_span.innerHTML = "<i class='fas fa-check'></i>"
                result_span.innerHTML = status;
            } else {
                upload_span.style.color = "#f50537";
                upload_span.innerHTML = "<i class='fas fa-xmark'></i> "+status;
            }
        } else {
            upload_span.style.color = "#f50537"
            upload_span.textContent = "Error";
        }
        await new Promise(r => setTimeout(r, 2000));
        upload_span.innerHTML = "";
    } else {
        console.log("error")
        upload_span.style.color = "#f50537";
        upload_span.innerHTML = "<i class='fas fa-xmark'></i> No file selected!";
    }
}