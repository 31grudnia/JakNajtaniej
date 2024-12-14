import axios from 'axios'


const BASE_URL = 'http://0.0.0.0:8000/jaknajtaniej/';
const LOGIN_URL = `${BASE_URL}api/token/`;

export const login = async (username, password) => {
    const response = await axios.post(LOGIN_URL,
        {username: username, password: password},
        {withCredentials: true}
    )

    return response.data.success
}