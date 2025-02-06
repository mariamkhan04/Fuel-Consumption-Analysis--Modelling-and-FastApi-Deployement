document.addEventListener("DOMContentLoaded", function() {
    // Ensure that the script is only running after the DOM is fully loaded
    const form = document.getElementById("predictForm");
    
    form.addEventListener("submit", function(e) {
        e.preventDefault();  // Prevent the default form submission (page reload)

        // Getting form data
        let formData = new FormData(form);

        // Sending data to backend
        fetch("/predict/", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            let resultDiv = document.querySelector(".result");

            // Check if the response contains an error
            if (data.detail) {
                resultDiv.innerHTML = `<p style="color:red;">Error: ${data.detail}</p>`;
            } else {
                resultDiv.innerHTML = `<p style="color:green;">Fuel Consumption Prediction: ${data.fuel_consumption_prediction} L/100km</p>`;
            }
        })
        .catch(error => {
            // Handle any errors that occur
            console.error("Error:", error);
            let resultDiv = document.querySelector(".result");
            resultDiv.innerHTML = `<p style="color:red;">Something went wrong! Please try again.</p>`;
        });
    });
});
