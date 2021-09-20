import {getAuth} from 'firebase/auth'
import { getFirestore } from 'firebase/firestore'
import {initializeApp} from 'firebase/app'
import {config} from'./firebase.config'
import { getStorage } from 'firebase/storage'


export const app = initializeApp(config);
export const db = getFirestore(app);
export const auth = getAuth();
export const storage = getStorage()

