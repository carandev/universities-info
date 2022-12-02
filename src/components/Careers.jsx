import React, { useEffect, useState } from 'react'

const Careers = ({ universityId }) => {
  const [careers, setCareers] = useState([])

  useEffect(() => {
    const fetchQuery = async () => {
      const response = await fetch(`http://localhost:8000/universities/${universityId}/careers`)
      const json = await response.json()

      setCareers(json)
    }

    fetchQuery()
  }, [universityId])

  return (
    <ul>
      {
        careers.map(({ Career }) => <li key={Career.id}>{Career.name}</li>)
      }
    </ul>
  )
}

export default Careers
