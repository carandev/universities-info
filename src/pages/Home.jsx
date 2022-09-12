import React, {useEffect, useState} from 'react';
import Header from "../components/Header.jsx";
import Footer from "../components/Footer.jsx";

const Home = () => {
  const [greet, setGreet] = useState({})

  useEffect(() => {
    fetch('http://localhost:8000')
      .then(response => response.json())
      .then(json => setGreet(json))
  }, [])

  return (
    <>
      <Header/>
      <main>
        <h2>Hi, {greet['Hello']}</h2>
      </main>
      <Footer/>
  </>
  )
};

export default Home;