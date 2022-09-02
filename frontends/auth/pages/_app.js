import { useEffect, useState } from 'react'

import { AuthProvider } from '../src/contexts/authContext'

function MyApp({ Component, pageProps }) {
  const [showChild, setShowChild] = useState(false)

  useEffect(() => {
    setShowChild(true)
  }, [])

  if (!showChild) {
    return null
  }

  return (
    <AuthProvider>
      <Component {...pageProps} />
    </AuthProvider>
  )
}

export default MyApp
