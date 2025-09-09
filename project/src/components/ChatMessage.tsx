import React from 'react';
import { User, Bot } from 'lucide-react';

interface Message {
  id: string;
  text: string;
  isUser: boolean;
  timestamp: Date;
  suggestions?: string[];
  intent?: string;
  confidence?: number;
}

interface ChatMessageProps {
  message: Message;
  onSuggestionClick: (suggestion: string) => void;
}

export const ChatMessage: React.FC<ChatMessageProps> = ({ message, onSuggestionClick }) => {
  return (
    <div className="space-y-3">
      <div className={`flex ${message.isUser ? 'justify-end' : 'justify-start'}`}>
        <div className={`flex items-start space-x-3 max-w-xs lg:max-w-md ${message.isUser ? 'flex-row-reverse space-x-reverse' : ''}`}>
          <div className={`p-2 rounded-full ${message.isUser ? 'bg-blue-600' : 'bg-gray-600'}`}>
            {message.isUser ? (
              <User className="h-4 w-4 text-white" />
            ) : (
              <Bot className="h-4 w-4 text-white" />
            )}
          </div>
          <div className={`p-3 rounded-2xl ${
            message.isUser 
              ? 'bg-blue-600 text-white rounded-br-md' 
              : 'bg-gray-100 text-gray-900 rounded-bl-md border border-gray-200'
          }`}>
            <p className="text-sm leading-relaxed">{message.text}</p>
            {message.confidence && !message.isUser && (
              <div className="mt-2 pt-2 border-t border-gray-200">
                <p className="text-xs text-gray-600">
                  Intent: {message.intent} ({Math.round(message.confidence * 100)}% confidence)
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
      
      {/* Suggestions */}
      {message.suggestions && message.suggestions.length > 0 && (
        <div className="flex flex-wrap gap-2 ml-12">
          {message.suggestions.map((suggestion, index) => (
            <button
              key={index}
              onClick={() => onSuggestionClick(suggestion)}
              className="px-3 py-1 text-xs bg-blue-50 hover:bg-blue-100 text-blue-700 rounded-full border border-blue-200 transition-colors duration-200 hover:scale-105 transform"
            >
              {suggestion}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};