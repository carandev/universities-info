import React, { useEffect, useState } from 'react'

import { Header, Footer } from '../components'

const Home = () => {
  const [universities, setUniversities] = useState([])

  const fetchQuery = async () => {
    const response = await fetch('http://localhost:8000/universities/')
    const json = await response.json()

    setUniversities(json)
  }

  useEffect(() => {
    fetchQuery()
  }, [])

  return (
    <>
      <Header/>
      <main className='flex gap-4 flex-wrap justify-center'>
        <section className='flex gap-4 flex-wrap justify-center max-w-xs'>
          {
          universities.map(({ University }) =>
            <div key={University.id} className='bg-yellow-400 p-4 rounded text-center'>
              {University.name}
            </div>
          )
        }
        </section>
      <img alt="Estudiantes en un salón" className='w-80' src="/home.svg"/>
      </main>
      <Footer/>
  </>
  )
}

export default Home
