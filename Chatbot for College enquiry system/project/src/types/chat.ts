export interface Message {
  id: string;
  text: string;
  isUser: boolean;
  timestamp: Date;
  suggestions?: string[];
  intent?: string;
  confidence?: number;
}

export interface ChatResponse {
  response: string;
  intent: string;
  confidence: number;
  suggestions: string[];
  timestamp: string;
  error?: boolean;
}

export interface ConversationContext {
  history_length: number;
  user_interests: string[];
  asked_topics: string[];
  message_count: number;
  session_duration: string;
}