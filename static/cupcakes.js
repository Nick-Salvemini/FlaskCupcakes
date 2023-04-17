async function getCupcake() {
    const id = $(this).data('id')
    await axios.get(`/api/cupcakes/${id}`)
}