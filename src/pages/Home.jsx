import React, { useEffect, useState } from 'react'

import Header from '../components/Header.jsx'
import Footer from '../components/Footer.jsx'

const Home = () => {
  const [greet, setGreet] = useState({})
  const [query, setQuery] = useState({})

  const fetchQuery = async () => {
    const response = await fetch('http://localhost:8000/items/2?q=de locos')
    const json = await response.json()

    setQuery(json)
  }

  useEffect(() => {
    fetch('http://localhost:8000')
      .then(response => response.json())
      .then(json => setGreet(json))
  }, [])

  return (
    <>
      <Header/>
      <main>
        <h2>Hi, {greet.Hello} -- Query: {query.q}</h2>
        <button onClick={fetchQuery}>Send Request</button>
      </main>
      <Footer/>
  </>
  )
}

export default Home
