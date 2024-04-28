import React from 'react'
import { useEffect, useState, useRef } from 'react'
import axios from 'axios'
import qs from 'qs'

const TransButton = ({ callback, cap }) => {
    const [languageOptions, setLanguageOptions] = useState([
        { code: 'en', name: 'English' },
        { code: 'fr', name: 'French' },
        { code: 'ar', name: 'Arabic' }
    ])
    const [to, setTo] = useState('en')
    const [translation, setTranslation] = useState('')

    const prevTo = useRef(to)

    const handleTranslate = async () => {
        const formData = qs.stringify({
            text: cap,
            from: 'auto',
            to: to
        })

        const options = {
            method: 'POST',
            url: 'https://google-translate113.p.rapidapi.com/api/v1/translator/text',
            headers: {
                'content-type': 'application/x-www-form-urlencoded',
                'X-RapidAPI-Key': 'd7331607admsh485c5bb480c8e52p1af2dfjsn2678b2dc3378',
                'X-RapidAPI-Host': 'google-translate113.p.rapidapi.com'
            },
            data: formData
        }

        for (let attempt = 0; attempt < 3; attempt++) {
            try {
                const response = await axios.request(options)
                if (response.data && response.data.trans) {
                    setTranslation(response.data.trans)
                    callback(response.data.trans)
                    return
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
                {/* {translation && <div className='translation-result'>{translation}</div>} */}
            </div>
        </>
    )
}

export default TransButton
