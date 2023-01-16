const upload_btn = document.querySelector("#upload-btn");
const upload_input = document.querySelector("#upload-input");
const upload_span = document.querySelector("#upload-span");
const result_span = document.querySelector("#result-span");

const select_functionality = document.querySelector("#select-functionality")

upload_btn.addEventListener("click", async () => await uploadFile());

async function uploadFile() {
    let functionality = select_functionality.value;
    let img = upload_input.files[0];

    if (typeof img !== 'undefined') {
        let formData = new FormData();
        formData.append("functionality", functionality);
        formData.append("image", img);

        upload_span.innerHTML = '<img src="./static/loader.gif" id="loading-gif" class="img-fluid" width="60"></img>';
        let response = await fetch("/media/upload", { method: "POST", body: formData });
        upload_span.innerHTML = "X";
        if (response.status == 200) {
            let res = await response.json()
            let flag = res[0];
            let status = res[1];
            console.log(flag, status)
            if (flag == true) {
                upload_span.style.color = "#32cd32";
                upload_span.innerHTML = "<i class='fas fa-check'></i>"
                result_span.innerHTML = status;
            } else {
                upload_span.style.color = "#f50537";
                upload_span.innerHTML = "<i class='fas fa-xmark'></i> " + status;
            }
        } else {
            upload_span.style.color = "#f50537"
            upload_span.textContent = "Error";
        }
    } else {
        console.log("error")
        upload_span.style.color = "#f50537";
        upload_span.innerHTML = "<i class='fas fa-xmark'></i> No file selected!";
    }
    await new Promise(r => setTimeout(r, 2000));
    upload_span.innerHTML = "X";
    upload_span.style.color = "transparent";
}

// On close or refresh
window.onbeforeunload = async function () {
    let response = await fetch("/account/logout", { method: "POST" });
}

// drop zone
document.querySelectorAll(".drop-zone-input").forEach((inputElement) => {
    const dropZoneElement = inputElement.closest(".drop-zone");
    dropZoneElement.addEventListener("click", (e) => {
        inputElement.click();
    });
    inputElement.addEventListener("change", (e) => {
        if (inputElement.files.length) {
            updateThumbnail(dropZoneElement, inputElement.files[0]);
        }
    });
    dropZoneElement.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropZoneElement.classList.add("drop-zone--over");
    });
    ["dragleave", "dragend"].forEach((type) => {
        dropZoneElement.addEventListener(type, (e) => {
            dropZoneElement.classList.remove("drop-zone--over");
        });
    });
    dropZoneElement.addEventListener("drop", (e) => {
        e.preventDefault();
        if (e.dataTransfer.files.length) {
            inputElement.files = e.dataTransfer.files;
            updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
        }
        dropZoneElement.classList.remove("drop-zone--over");
    });
});
function updateThumbnail(dropZoneElement, file) {
    let thumbnailElement = dropZoneElement.querySelector(".drop-zone-thumb");
    // First time - remove the prompt
    if (dropZoneElement.querySelector(".drop-zone-prompt")) {
        dropZoneElement.querySelector(".drop-zone-prompt").remove();
    }
    // First time - there is no thumbnail element, so lets create it
    if (!thumbnailElement) {
        thumbnailElement = document.createElement("div");
        thumbnailElement.classList.add("drop-zone-thumb");
        dropZoneElement.appendChild(thumbnailElement);
    }
    thumbnailElement.dataset.label = file.name;
    // Show thumbnail for image files
    if (file.type.startsWith("image/")) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
        };
    } else {
        thumbnailElement.style.backgroundImage = null;
    }
} 