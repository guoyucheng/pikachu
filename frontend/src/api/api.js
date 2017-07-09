import axios from 'axios';
var querystring = require('querystring');
var isProduction = process.env.NODE_ENV === 'production';
let base = 'http://localhost:8010';
if (isProduction) {
    base = ""
}


// export const requestLogin = params => { return axios.post(`${base}/rest/account/api/login`,  querystring.stringify(params)).then(res => res.data); };

// export const getPictureList = params => { 
//     return axios.get(`${base}/rest/album/api/picture_list?` + querystring.stringify(params)).then(res => res.data); 
// };

// export const downloadPic = params => {
//     window.open(`${base}/rest/album/api/picture_download/?`+querystring.stringify(params) , '_blank');
// }


// export const requestLogout = params => { return axios.post(`${base}/rest/account/api/logout`).then(res => res.data); };


export const getPlateformList = params => {
    return axios.get(`${base}/platform/get_platforms/?` + querystring.stringify(params)).then(res => res.data); 
} 

export const getLiveList = params => {
    return axios.post(`${base}/platform/get_lives/?` , querystring.stringify(params)).then(res => res.data); 
} 