import Vue from 'vue'
import VueRouter from 'vue-router'
import App from '../App'
import Login from '../components/Login'
import Register from '../components/Register'
import Home from '../components/Home'
import Like from '../components/Like'
import Profile from '../components/Profile'
import ApiTest from '../components/ApiTest'

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
  {
    path: '/like',
    name: 'like',
    component: Like
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/api-test',
    name: 'api-test',
    component:ApiTest
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
