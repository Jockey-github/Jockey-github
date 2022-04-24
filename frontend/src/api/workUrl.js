import request from '@/utils/request'

export function getlist(){
    return request({
        url:'api/show_urls',
        method:'get'

})
}

export function addbook(book_name) {
    return request({
      url: '/api/show_urls',
      method: 'get',
      params: { book_name }
    })
  }