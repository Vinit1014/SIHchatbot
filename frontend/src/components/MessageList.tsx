import React from 'react';

interface Message {
    text: string;
    type: 'question' | 'answer';
  }
  
interface MessageListProps {
    data: Message;
}

const MessageList: React.FC<MessageListProps> = ({ data }) => {

    return (
        <div className='p-4'>
                <div className={`flex ${data.type === 'question' ? 'justify-end' : 'justify-start'} mb-2`}>
                    <div className={`p-3 rounded-lg max-w-xs text-left ${data.type === 'question' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'}`}>
                    {data.text}
                    </div>
                </div>
        </div>
    )
}

export default MessageList