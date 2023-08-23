document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    const uploadButton = document.getElementById('uploadButton');
    const resultSection = document.getElementById('resultSection');
    const resultDiv = document.getElementById('result');

    uploadButton.addEventListener('click', () => {
        // Check if a file is selected
        if (fileInput.files.length === 0) {
            alert('Please select a file.');
            return;
        }

        const file = fileInput.files[0];
        const formData = new FormData();
        formData.append('csvFile', file);

        // Specify the host and port for the Flask server
        const host = '127.0.0.1'; // Update with Flask server's host
        const port = 8000;       // Update with Flask server's port

        fetch(`http://${host}:${port}/upload`, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Display the result received from the back end
            resultDiv.textContent = data.result;

            // Show the "Analysis Result" section
            resultSection.style.display = 'block';
        })
        .catch(error => {
            // Handle any errors that occurred during the file upload
            alert('Error occurred during file upload.');
            console.error('Error occurred during file upload:', error);
        });
    });
});