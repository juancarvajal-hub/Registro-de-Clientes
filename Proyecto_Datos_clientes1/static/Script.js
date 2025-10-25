document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    form.addEventListener("submit", (event) => {
        event.preventDefault(); // evita recargar la página

        fetch(form.action, {
            method: form.method,
            body: new FormData(form),
        })
        .then(response => {
            if (response.ok) {
                alert("✅ ¡Gracias! Tu información ha sido enviada correctamente.");
                form.reset(); // limpia los campos
            } else {
                alert("⚠️ Ocurrió un problema al enviar los datos.");
            }
        })
        .catch(() => {
            alert("⚠️ No se pudo conectar con el servidor.");
        });
    });

    // Efecto visual del botón Cerrar
    const closeBtn = document.getElementById("close-btn");
    if (closeBtn) {
        closeBtn.addEventListener("mouseover", () => {
            closeBtn.style.backgroundColor = "#c0392b";
        });
        closeBtn.addEventListener("mouseout", () => {
            closeBtn.style.backgroundColor = "#e74c3c";
        });
        closeBtn.addEventListener("click", () => {
            fetch("/cerrar", { method: "POST" });
            window.close();
        });
    }
});