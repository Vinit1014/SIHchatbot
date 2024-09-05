
import React, { useState, useEffect, useContext } from 'react';
import Navbar from './ui/Navbar';
import { ChatContext } from './ChatContext';
import MessageList from './MessageList';
import FAQs from './FAQsection';

const Chat = () => {
    const [isSidebarOpen, setIsSidebarOpen] = useState(false);
    const [inputValue, setInputValue] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const {messages, addMessage} = useContext(ChatContext)!;


    useEffect(()=>{
        console.log(inputValue);
    },[inputValue])

    const toggleSidebar = () => {
        setIsSidebarOpen(!isSidebarOpen);
    };

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setInputValue(event.target.value);
    };

    const implementSearch = (event: React.FormEvent) => {
        event.preventDefault();
        if (inputValue.trim()) {
            addMessage(inputValue, 'question');
            setInputValue('');

            setIsLoading(true);
            setTimeout(() => {
                addMessage('This is a simulated answer.', 'answer');
                setIsLoading(false);
            }, 1500);
        }
    };

    return (
        <div className='flex mt-0 border-2 w-full h-screen'>
            {/* Sidebar */}
            <div
                className={`${
                    isSidebarOpen ? 'block' : 'hidden'
                } md:block w-full md:w-1/4 bg-blue-500 text-white p-4`}
            >
                {/* <h2 className="text-lg font-bold">Sidebar</h2>
                <p>This is the left component.</p> */}
                <FAQs/>
            </div>

            {/* Main Content */}
            <div className='flex-1 border-2'>
                <div className='p-4 overflow-y-scroll border-4 h-5/6  justify-between'>
                    {/* Navbar with Toggle Sidebar */}
                    <div onClick={toggleSidebar} className='w-full'>
                        <Navbar />
                    </div>
                    {messages.map((data, index) => (
                        <MessageList key={index} data={data} />
                    ))}

                    {/* Loading state */}
                    {isLoading && (
                        <div className='flex justify-start mx-4 m-2'>
                            <p className='text-gray-500'>Loading...</p>
                        </div>
                    )}
                </div>

                {/* Search Input with Button */}
                <div className='m-1 flex items-center'>
                    <input
                        placeholder='Search here'
                        className='border-2 w-full rounded-full p-4 shadow-md focus:outline-none focus:ring-2 focus:ring-neutral-200 bg-gray-100'
                        value={inputValue}
                        onChange={handleInputChange}
                    />
                    <button
                        className={`ml-1 p-4 rounded-full text-white shadow-md ${
                            inputValue ? 'bg-blue-500 hover:bg-neutral-500 cursor-pointer' : 'bg-gray-300 cursor-not-allowed'
                        }`}
                        disabled={!inputValue}
                        onClick={implementSearch}
                    >
                        →
                    </button>
                </div>

            </div>
        </div>
    );
};

export default Chat;
