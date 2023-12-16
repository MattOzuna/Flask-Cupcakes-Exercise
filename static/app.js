$('button').on('click', addCupcake)
form = document.querySelector('form')


async function addCupcake(e) {
    e.preventDefault()
    
    flavor = $('input[name=flavor]').val()
    size = $('input[name=size]').val()
    rating = $('input[name=rating]').val()
    image = $('input[name=image]').val()
    form.reset()

    response = await axios.post('/api/cupcakes', {
        'flavor': flavor,
        'size': size,
        'rating': rating,
        'image': image
    })

    $(`<div class="col-md-3">
            <img src="${response.data.cupcake.image}" class="img-thumbnail" alt="${response.data.cupcake.flavor} cupcake">
            <li>${response.data.cupcake.flavor} cupcake</li>
        </div>`).appendTo('ul')
}