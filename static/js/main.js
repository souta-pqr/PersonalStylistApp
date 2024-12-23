document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    var formData = new FormData();
    var fileInput = document.getElementById('image-upload');
    formData.append('file', fileInput.files[0]);
    formData.append('season', document.getElementById('season').value);
    formData.append('occasion', document.getElementById('occasion').value);

    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('uploaded-image').src = data.image_path;
        document.getElementById('style').textContent = data.style;
        document.getElementById('recommendation').textContent = data.recommendation;
        document.getElementById('detected-items').textContent = data.detected_items.join(', ');
        document.getElementById('result').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
});