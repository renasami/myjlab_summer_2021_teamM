import 'firebase/auth'
import 'firebase/firestore'
import fb from 'firebase/app'
import config from'./firebase.config'


export const firebase = !fb.apps.length ? fb.initializeApp(config) : fb.app()
export const firestore = firebase.firestore()