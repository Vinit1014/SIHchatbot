import React, { useState } from 'react';

const FAQs = () => {
    const [openFAQIndex, setOpenFAQIndex] = useState<number | null>(null);

    const faqs = [
        {
            question: 'What is React?',
            answer: 'React is a JavaScript library for building user interfaces.',
        },
        {
            question: 'What is Next.js?',
            answer: 'Next.js is a React framework that provides infrastructure and simple development experience for server-side rendering and static site generation.',
        },
        {
            question: 'What is Tailwind CSS?',
            answer: 'Tailwind CSS is a utility-first CSS framework that allows for rapid UI development with predefined classes.',
        },
    ];

    const toggleFAQ = (index: number) => {
        setOpenFAQIndex(openFAQIndex === index ? null : index);
    };

    return (
        <div className={`md:block w-full bg-blue-500 text-white p-4`}>
            <h2 className="text-lg font-bold mb-4">FAQs</h2>
            {faqs.map((faq, index) => (
                <div key={index} className='mb-4'>
                    <div className='flex justify-between items-center'>
                        <p className='font-semibold'>{faq.question}</p>
                        <button
                            className='bg-white text-blue-500 px-2 py-1 rounded focus:outline-none'
                            onClick={() => toggleFAQ(index)}
                        >
                            {openFAQIndex === index ? '<-' : '->'}
                        </button>
                    </div>
                    {openFAQIndex === index && (
                        <p className='justify-start mt-2 bg-blue-400 p-2 rounded'>{faq.answer}</p>
                    )}
                </div>
            ))}
        </div>
    );
};

export default FAQs;
