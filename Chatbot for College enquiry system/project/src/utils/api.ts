const API_BASE_URL = '';

export class ChatAPI {
  static async sendMessage(message: string): Promise<any> {
    const response = await fetch(`${API_BASE_URL}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.json();
  }

  static async resetConversation(): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/api/reset`, {
      method: 'POST',
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
  }

  static async getSuggestions(): Promise<any> {
    const response = await fetch(`${API_BASE_URL}/api/suggestions`);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.json();
  }
}