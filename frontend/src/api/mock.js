import request from '@/utils/request'

export function getList(){
    return request({
        url:'/api/show_mock/',
        method:'get'

})
}

export function addmock(mock_name) {
    return request({
      url: '/api/add_mock/',
      method: 'get',
      params: { mock_name }
    })
  }