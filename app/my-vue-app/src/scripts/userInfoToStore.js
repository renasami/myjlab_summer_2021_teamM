import {app} from '../firebase'
import { getAuth } from 'firebase/auth'
import store from '../store'
app


export const isLogin = () => {
    const user = getAuth()
    if (user) return true
    else  return false
}

export const toStore = () => {
    const valid = isLogin()
    if(!valid) return
    const user = getAuth()
    user.onAuthStateChanged(u =>{
        if (user) {
            console.log(user)
            store.commit("setUsername",u.displayName)
            //@よりも前を切り出し
            if(!u.displayName) store.commit("setUsername", u.email.substring(0,u.email.indexOf("@")))
        }
    });
}