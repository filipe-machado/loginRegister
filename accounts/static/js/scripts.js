$('.toast').toast('show')

const searchBtn = $('#search-btn')
const searchForm = $('#search-form')

$(searchBtn).on('click', () => {
    searchForm.submit()
})