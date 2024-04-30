// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "${{ secrets.FIREBASE_API_KEY }}",
  authDomain: "ddlbx-web.firebaseapp.com",
  projectId: "ddlbx-web",
  storageBucket: "ddlbx-web.appspot.com",
  messagingSenderId: "239903105303",
  appId: "1:239903105303:web:a5271c49e15dbcc0e71752"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);