import React from 'react'
import { useEffect, useState, useRef } from 'react'
import axios from 'axios' // Import axios

const TransButton = ({ callback, cap }) => {
    const [languageOptions, setLanguageOptions] = useState([
        { code: 'en', name: 'English' },
        { code: 'fr-ca', name: 'French' },
        { code: 'ar', name: 'Arabic' }
    ])
    const [to, setTo] = useState('en')

    const prevTo = useRef(to)

    const handleTranslate = async () => {
        const options = {
            method: 'POST',
            url: 'https://google-translate1.p.rapidapi.com/language/translate/v2',
            headers: {
                'content-type': 'application/json',
                'X-RapidAPI-Key': 'd7331607admsh485c5bb480c8e52p1af2dfjsn2678b2dc3378',
                'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
            },
            data: JSON.stringify({
                q: cap,
                source: 'en',
                target: to
            })
        }

        for (let attempt = 0; attempt < 3; attempt++) {
            try {
                const response = await axios.request(options)
                if (response.data) {
                    const result = response.data.data.translations[0].translatedText
                    callback(result)
                    return // Exit after successful response
                }
            } catch (error) {
                console.error('Translation error:', error.message)
                if (attempt === 2) {
                    // Last attempt
                    alert('Failed to translate. Please try again later.')
                }
                // Wait 2 seconds before retrying
                await new Promise((resolve) => setTimeout(resolve, 2000))
            }
        }
    }

    const handleLanguageChange = (e) => {
        setTo(e.target.value)
    }

    useEffect(() => {
        if (prevTo.current !== to) {
            console.log(to)
            prevTo.current = to
        }
    }, [to])

    return (
        <>
            <div style={{ margin: '14px 2px', marginLeft: '157px' }}>
                <select onChange={handleLanguageChange}>
                    {languageOptions.map((opt) => (
                        <option key={opt.code} value={opt.code}>
                            {opt.name}
                        </option>
                    ))}
                </select>
            </div>
            <div>
                <button className='translate-btn' onClick={handleTranslate}>
                    Translate
                </button>
            </div>
        </>
    )
}

export default TransButton
