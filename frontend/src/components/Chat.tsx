
// import React, { useState, useEffect } from 'react';
// import Navbar from './ui/Navbar';

// const Chat = () => {
//     const [isSidebarOpen, setIsSidebarOpen] = useState(false);
//     const [inputValue, setInputValue] = useState('');

//     useEffect(()=>{
//         console.log(inputValue);
//     },[inputValue])

//     const toggleSidebar = () => {
//         setIsSidebarOpen(!isSidebarOpen);
//     };

//     const handleInputChange = (event:any) => {
//         setInputValue(event.target.value);
//     };

//     return (
//         <div className='flex border-2 border-red-200 w-full h-screen'>
//             {/* Sidebar */}
//             <div
//                 className={`${
//                     isSidebarOpen ? 'block' : 'hidden'
//                 } md:block w-full md:w-1/4 bg-blue-500 text-white p-4`}
//             >
//                 <h2 className="text-lg font-bold">Sidebar</h2>
//                 <p>This is the left component.</p>
//             </div>

//             {/* Main Content */}
//             <div className='flex-1 border-2 border-violet-400'>
//                 <div className='p-4 overflow-y-scroll border-4 border-black h-5/6 flex justify-between'>
//                     {/* Navbar with Toggle Sidebar */}
//                     <div onClick={toggleSidebar} className='w-full'>
//                         <Navbar />
//                     </div>
//                 </div>

//                 {/* Search Input with Button */}
//                 <div className='m-1 flex items-center'>
//                     <input
//                         placeholder='Search here'
//                         className='border-2 border-pink-800 w-full rounded-full p-4'
//                         value={inputValue}
//                         onChange={handleInputChange}
//                     />
//                     <button
//                         className={`ml-1 p-4 rounded-full text-white ${
//                             inputValue ? 'bg-blue-500 cursor-pointer' : 'bg-gray-300 cursor-not-allowed'
//                         }`}
//                         disabled={!inputValue}
//                     >
//                         →
//                     </button>
//                 </div>
//             </div>
//         </div>
//     );
// };

// export default Chat;

import React, { useState } from 'react';
import Navbar from './ui/Navbar';

const Chat = () => {
    const [isSidebarOpen, setIsSidebarOpen] = useState(false);
    const [inputValue, setInputValue] = useState('');
    const [messages, setMessages] = useState([]);

    const toggleSidebar = () => {
        setIsSidebarOpen(!isSidebarOpen);
    };

    const handleInputChange = (event) => {
        setInputValue(event.target.value);
    };

    const handleSendMessage = () => {
        if (inputValue.trim()) {
            setMessages([...messages, { text: inputValue, type: 'question' }]);
            setInputValue('');

            // Simulate an answer (for testing)
            setTimeout(() => {
                setMessages((prevMessages) => [
                    ...prevMessages,
                    { text: 'This is a simulated answer.', type: 'answer' },
                ]);
            }, 500);
        }
    };

    return (
        <div className='flex border-2 border-red-200 w-full h-screen'>
            {/* Sidebar */}
            <div
                className={`${
                    isSidebarOpen ? 'block' : 'hidden'
                } md:block w-full md:w-1/4 bg-blue-500 text-white p-4`}
            >
                <h2 className="text-lg font-bold">Sidebar</h2>
                <p>This is the left component.</p>
            </div>

            {/* Main Content */}
            <div className='flex-1 border-2 border-violet-400'>
                <div className='p-4 overflow-y-scroll border-4 border-black h-5/6 flex justify-between'>
                    {/* Navbar with Toggle Sidebar */}
                    <div onClick={toggleSidebar} className='w-full'>
                        <Navbar />
                    </div>
                </div>

                {/* Messages Component */}
                <div className='flex-1 p-4 border-2 border-gray-300 overflow-y-auto'>
                    {messages.map((message, index) => (
                        <div
                            key={index}
                            className={`my-2 p-2 rounded-lg max-w-xs ${
                                message.type === 'question' ? 'bg-blue-100 self-end' : 'bg-green-100 self-start'
                            }`}
                        >
                            {message.text}
                        </div>
                    ))}
                </div>

                {/* Search Input with Button */}
                <div className='m-1 flex items-center'>
                    <input
                        placeholder='Search here'
                        className='border-2 border-pink-800 w-full rounded-full p-4'
                        value={inputValue}
                        onChange={handleInputChange}
                    />
                    <button
                        className={`ml-1 p-4 rounded-full text-white ${
                            inputValue ? 'bg-blue-500 cursor-pointer' : 'bg-gray-300 cursor-not-allowed'
                        }`}
                        disabled={!inputValue}
                        onClick={handleSendMessage}
                    >
                        →
                    </button>
                </div>
            </div>
        </div>
    );
};

export default Chat;
