import Vue from 'vue'
import VueRouter from 'vue-router'
import App from '../App'
import Login from '../components/Login'
import Register from '../components/Register'
import Home from '../components/Home'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'app',
    component: App,
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
