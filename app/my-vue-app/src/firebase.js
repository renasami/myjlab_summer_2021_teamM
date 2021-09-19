import {getAuth} from 'firebase/auth'
import { getFirestore } from 'firebase/firestore'
import {initializeApp} from 'firebase/app'
import {config} from'./firebase.config'



export const app = initializeApp(config);
export const db = getFirestore();
export const auth = getAuth();

