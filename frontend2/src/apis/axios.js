import axios from 'axios'

const instance = axios.create({ baseURL: 'http://localhost:5000' })
const path = "http://localhost:5000"

const getTodayNumber = async () => {
    try { 
        const response = await instance.get("/home") 
        return response.data;
    }
    catch (error) {
        return 'error'
    } 
}

const getAnalysis = async (arg) => {
    try { 
        const response = await instance.get("/analysis", { params: { arg } }) 
        return response.data;
    }
    catch (error) {
        return 'error'
    } 
}

export { getTodayNumber, getAnalysis };