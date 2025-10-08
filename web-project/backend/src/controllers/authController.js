class AuthController {
    constructor(userModel) {
        this.userModel = userModel;
    }

    async register(req, res) {
        const { username, password } = req.body;
        try {
            const newUser = await this.userModel.create({ username, password });
            res.status(201).json({ message: 'User registered successfully', user: newUser });
        } catch (error) {
            res.status(500).json({ message: 'Error registering user', error });
        }
    }

    async login(req, res) {
        const { username, password } = req.body;
        try {
            const user = await this.userModel.findOne({ username });
            if (!user || user.password !== password) {
                return res.status(401).json({ message: 'Invalid credentials' });
            }
            res.status(200).json({ message: 'Login successful', user });
        } catch (error) {
            res.status(500).json({ message: 'Error logging in', error });
        }
    }
}

export default AuthController;