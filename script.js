window.addEventListener("load", () => {
    console.log("true");
    document.querySelector("#send_order").addEventListener("click", () => {
        let pib = document.querySelector("#pib").value;
        let subject = document.querySelector("#subject").value;
        let university = document.querySelector("#university").value;
        let course = document.querySelector("#course").value;
        let contacts = document.querySelector("#contacts").value;
        let task = document.querySelector("#task").value;
        let attachment = document.querySelector("#attachment").files[0];
        let deadline = document.querySelector("#deadline").value;
        let formData = new FormData();
        formData.append("pib", pib);
        formData.append("subject", subject);
        formData.append("university", university);
        formData.append("course", course);
        formData.append("contacts", contacts);
        formData.append("task", task);
        formData.append("attachment", attachment);
        formData.append("deadline", deadline);

        fetch("/send_order", {
            method: "POST",
            body: formData,
        })
            .then((response) => {
                if (response.ok) {
                    console.log("Дані успішно відправлені на сервер");
                } else {
                    console.log(
                        "Сталася помилка при відправленні даних на сервер"
                    );
                }
            })
            .catch((error) => {
                console.error("Сталася помилка:", error);
            });
    });
});
