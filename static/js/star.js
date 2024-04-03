const ratingItemsList = document.querySelectorAll('.rating__item')
const ratingItemsArray = Array.prototype.slice.call(ratingItemsList)
const starsCount = document.getElementById('star')
const address = document.getElementById('address')
const form = document.getElementById('contact-form')

function showPosition(position) {
    console.log("Latitude: " + position.coords.latitude, "Longitude: " + position.coords.longitude)
}

ratingItemsArray.forEach(item =>
    item.addEventListener('click', () => {
            const {itemValue} = item.dataset
            item.parentNode.dataset.totalValue = itemValue
            starsCount.value = itemValue
            address.value = navigator.geolocation.getCurrentPosition(showPosition);
            console.log(address)
            window.location.navigator
        }
    )
)

form.addEventListener('submit', () => {
    $.ajax({
        url: 'review/',
        type: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
        },

        data: {
            team: $('#team').val(),
            text: $('#review').val(),
            user: $('#username').val(),
            star: $('#star').val(),
        },

        // handle a successful response
        success: function (json) {
            // remove the value from the input
            $('#team').val(''),
                $('#star').val(''),
                $('#review').val(''),
                console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },
        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText);
        }
    })
    window.location.reload()
})



