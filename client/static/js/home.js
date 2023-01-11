const upload_btn = document.querySelector("#upload-btn");
const upload_input = document.querySelector("#upload-input");
const upload_span = document.querySelector("#upload-span");

const select_functionality = document.querySelector("#select-functionality")

upload_btn.addEventListener("click", async () => await uploadFile());

async function uploadFile() {
    let functionality = select_functionality.value;

    let img = upload_input.files[0];
    console.log(img)
    
    if (typeof myVar !== 'undefined') {
        let formData = new FormData();
        formData.append("image", img);

        let response = await fetch("/upload?functionality="+functionality, {method: "POST", body:formData});
        if (response.status == 200) {
            let res = await response.json()
            let flag = res[0];
            let status = res[1];
            console.log(flag, status)
            if (flag == 0) {
                console.log("done")
                upload_span.style.color = "#32cd32";
                upload_span.innerHTML = "<i class='fas fa-check'></i>"
            } else {
                console.log("failed")
                upload_span.style.color = "#f50537";
                upload_span.innerHTML = "<i class='fas fa-xmark'></i> "+status;
            }
        } else {
            console.log("error")
            upload_span.style.color = "#f50537"
            upload_span.textContent = "Error";
        }
        await new Promise(r => setTimeout(r, 2000));
        upload_span.textContent = "";
    } else {
        console.log("error")
                upload_span.style.color = "#f50537";
                upload_span.innerHTML = "<i class='fas fa-xmark'></i> No file selected!";
    }
}